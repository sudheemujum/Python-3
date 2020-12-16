class movie():

    def __init__(self,title,hero,heroine):
        self.title=title
        self.hero=hero
        self.heroine=heroine

    def info(self):
        print('The name of the movie is:',self.title)
        print('The hero of the movie is:',self.hero)
        print('The heroine of the movie is:',self.heroine)


movie_list=[]

while True:
    title=input('Enter the name of the movie:')
    hero=input('Enter the name of the hero:')
    heroine=input('Enter the name of the heroine:')
    m=movie(title,hero,heroine)
    movie_list.append(m)
    print('Movie appended successfully to list', end='\n')
    option=input('Enter more movie details (Yes/No):')
    if option.lower()=='no':
        break

for movies in movie_list:
    movies.info()
    print('')
    
