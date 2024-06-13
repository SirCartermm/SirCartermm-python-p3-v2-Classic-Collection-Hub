#app.py
import click
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.supercar import Base, Supercar, Vote, Comment

engine = create_engine('sqlite:///supercars.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

@click.group()
def cli():
    """Supercar CLI"""
    pass

@cli.command()
def list_supercars():
    """List all supercars"""
    session = Session()
    supercars = session.query(Supercar).all()
    for supercar in supercars:
        click.echo(f"{supercar.name} ({supercar.description})")

@cli.command()
@click.argument('supercar_id', type=int)
def like_supercar(supercar_id):
    """Like a supercar"""
    session = Session()
    supercar = session.query(Supercar).get(supercar_id)
    if supercar:
        vote = Vote(supercar_id=supercar_id, vote_type='like')
        session.add(vote)
        session.commit()
        click.echo(f"Liked supercar {supercar_id} successfully!")
    else:
        click.echo("Supercar not found!")

@cli.command()
@click.argument('supercar_id', type=int)
@click.argument('comment_text', type=str)
def comment_supercar(supercar_id, comment_text):
    """Comment on a supercar"""
    session = Session()
    supercar = session.query(Supercar).get(supercar_id)
    if supercar:
        comment = Comment(supercar_id=supercar_id, comment_text=comment_text)
        session.add(comment)
        session.commit()
        click.echo(f"Commented on supercar {supercar_id} successfully!")
    else:
        click.echo("Supercar not found!")

if __name__ == '__main__':
    cli()