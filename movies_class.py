class movie:

    def __init__(self,title,hero,heroine):
        self.title=title
        self.hero=hero
        self.heroine=heroine

    def info(self):
        print('Name of the movie:',self.title)
        print('Name of the hero:',self.hero)
        print('Name of the heroine:',self.heroine)

movie_list=[]

while True:
    title=input('Enter the name of the movie:')
    hero=input('Enter the name of the hero:')
    heroine=input('Enter the name of the heroine:')
    m=movie(title,hero,heroine)
    movie_list.append(m)
    print('Movie is appended successfully',end='\n')
    option=input('Enter more movie details (Yes/No):')
    if option.lower()=='no':
        break

for movies in movie_list:
    movies.info()
    print('')
