#app.py
import click
from sqlalchemy.orm import sessionmaker
from models.supercar import Base, Supercar, User, Vote, Comment

engine = create_engine('sqlite:///supercars.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

@click.group()
def cli():
    pass

@cli.command()
def list_supercars():
    session = Session()
    supercars = session.query(Supercar).all()
    for supercar in supercars:
        click.echo(supercar.name)

@cli.command()
@click.argument('supercar_id', type=int)
def like_supercar(supercar_id):
    session = Session()
    vote = Vote(supercar_id=supercar_id, vote_type='like')
    session.add(vote)
    session.commit()

@cli.command()
@click.argument('supercar_id', type=int)
@click.argument('comment_text', type=str)

def comment_supercar(supercar_id, comment_text):
    session = Session()
    comment = Comment(supercar_id=supercar_id, comment_text=comment_text)
    session.add(comment)
    session.commit()

if __name__ == '__main__':
    cli()