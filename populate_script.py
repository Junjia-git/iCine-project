import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                    'django_movie.settings')
                    
import django
django.setup()

from myapp.models import ClassifyModel, MovieModel




def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories. # This might seem a little bit confusing, but it allows us to iterate # through each data structure, and add the data to our models.
    action_movies = [
        {'name': 'Braveheart','detail': 'When his secret bride is executed for assaulting an English soldier who tried to rape her, William Wallace begins a revolt against King Edward I of England.' ,
        'pic':'image/28.jpg','actor':'Mel Gibson, Sophie Marceau, Patrick McGoohan','duration':178,'star':4.2,"publish_time":"1995-05-08"},
        {'name': 'Fast & Furious: Hobbs & Shaw','detail': 'Lawman Luke Hobbs (Dwayne "The Rock" Johnson) and outcast Deckard Shaw (Jason Statham) form an unlikely alliance when a cyber-genetically enhanced villain threatens the future of humanity.' ,
        'pic':'image/19.jpg','actor':'Dwayne Johnson, Jason Statham, Idris Elba','duration':137,'star':3.3,"publish_time":"2019-08-23"},
        {'name': 'Mulan','detail': 'A young Chinese maiden disguises herself as a male warrior in order to save her father. A live-action feature film based on Disneys Mulan.' ,
        'pic':'image/10.jpg','actor':'Yifei Liu, Donnie Yen, Jet Li','duration':115,'star':4.5,"publish_time":"2020-03-27"} ]

    animation_movies = [
        {'name': 'Your Name','detail': 'Two strangers find themselves linked in a bizarre way. When a connection forms, will distance be the only thing to keep them apart?	' ,
        'pic':'image/27.jpg','actor':'Ryûnosuke Kamiki, Mone Kamishiraishi, Ryô Narita','duration':106,'star':4.3,"publish_time":"2016-12-02"},
        {'name': 'WALL·E','detail': 'In the distant future, a small waste-collecting robot inadvertently embarks on a space journey that will ultimately decide the fate of mankind.' ,
        'pic':'image/26.jpg','actor':'Ben Burtt, Elissa Knight, Jeff Garlin','duration':98,'star':4.5,"publish_time":"2008-07-18"},
        {'name': 'Onward','detail': 'Set in a suburban fantasy world, two teenage elf brothers embark on a quest to discover if there is still magic out there.' ,
        'pic':'image/18.jpg','actor':'Tom Holland, Chris Pratt, Julia Louis-Dreyfus','duration':102,'star':3.7,"publish_time":"2020-03-06"} ]

    comedy_movies = [
        {'name': '3 Idiots','detail': 'Two friends are searching for their long lost companion. They revisit their college days and recall the memories of their friend who inspired them to think differently, even as the rest of the world called them "idiots".' ,
        'pic':'image/33.jpg','actor':'Aamir Khan, Madhavan, Mona Singh','duration':170,'star':4.4,"publish_time":"2009-12-08"},
        {'name': 'Cats','detail': 'A tribe of cats called the Jellicles must decide yearly which one will ascend to the Heaviside Layer and come back to a new Jellicle life.' ,
        'pic':'image/29.jpg','actor':'Jennifer Hudson, Judi Dench, Taylor Swift','duration':110,'star':2.1,"publish_time":"2019-12-20"} ]
    
    rommancy_movies = [
        {'name': 'Amélie','detail': 'Amélie is an innocent and naive girl in Paris with her own sense of justice. She decides to help those around her and, along the way, discovers love.' ,
        'pic':'image/34.jpg','actor':'Audrey Tautou, Mathieu Kassovitz, Rufus','duration':122,'star':4.2,"publish_time":"2001-10-05"},
        {'name': 'Titanic','detail': 'A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.' ,
        'pic':'image/21.jpg','actor':'Leonardo DiCaprio, Kate Winslet, Billy Zane','duration':194,'star':5.0,"publish_time":"1998-04-03"} ]

    sci_movies = [
        {'name': 'Avengers: Infinity War','detail': 'The Avengers and their allies must be willing to sacrifice all in an attempt to defeat the powerful Thanos before his blitz of devastation and ruin puts an end to the universe.' ,
        'pic':'image/34.jpg','actor':'Robert Downey Jr., Chris Hemsworth, Mark Ruffalo','duration':122,'star':4.2,"publish_time":"2001-10-05"},
        {'name': 'Star Wars: The Rise of Skywalker','detail': 'The surviving members of the resistance face the First Order once again, and the legendary conflict between the Jedi and the Sith reaches its peak bringing the Skywalker saga to its end.' ,
        'pic':'image/20.jpg','actor':'Carrie Fisher, Mark Hamill, Adam Driver','duration':142,'star':3.4,"publish_time":"2019-12-20"} ]

    horror_movies = [
        {'name': 'The Shining','detail': 'Amélie is an innocent and naive girl in Paris with her own sense of justice. She decides to help those around her and, along the way, discovers love.' ,
        'pic':'image/31.jpg','actor':'Jack Nicholson, Shelley Duvall, Danny Lloyd','duration':146,'star':4.3,"publish_time":"1980-10-05"},
        {'name': 'The Invisible Man','detail': 'When Cecilias abusive ex takes his own life and leaves her his fortune, she suspects his death was a hoax. As a series of coincidences turn lethal, Cecilia works to prove that she is being hunted by someone nobody can see.' ,
        'pic':'image/16.jpg','actor':'Elisabeth Moss, Oliver Jackson-Cohen, Harriet Dyer','duration':124,'star':3.5,"publish_time":"2020-02-28"} ]
    
    adv_movies = [
        {'name': 'Inception','detail':'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O' ,
        'pic':'image/23.jpg','actor':'Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page','duration':148,'star':4.8,"publish_time":"2010-09-01"},
        {'name': 'Birds of Prey','detail': 'After splitting with the Joker, Harley Quinn joins superheroes Black Canary, Huntress and Renee Montoya to save a young girl from an evil crime lord.' ,
        'pic':'image/13.jpg','actor':'Margot Robbie, Rosie Perez, Mary Elizabeth Winstead','duration':109,'star':3.6,"publish_time":"2020-02-07"} ]
    
    drama_movies = [
        {'name': 'The Shawshank Redemption','detail':'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.' ,
        'pic':'image/22.jpg','actor':'Tim Robbins, Morgan Freeman, Bob Gunton','duration':142,'star':5,"publish_time":"1995-02-17"},
        {'name': 'Parasite','detail': 'A poor family, the Kims, con their way into becoming the servants of a rich family, the Parks. But their easy life gets complicated when their deception is threatened with exposure.' ,
        'pic':'image/12.jpg','actor':'Kang-ho Song, Sun-kyun Lee, Yeo-jeong Jo','duration':136,'star':4.5,"publish_time":"2020-02-07"} ]
    
    
    cats = {'Action': {'movies': action_movies},
            'Animation': {'movies': animation_movies},
            'Comedy': {'movies': comedy_movies}, 
            'Rommance':{'movies':rommancy_movies},
            'Sci-Fi/Fantasy' :{'movies':sci_movies},
            'Horror' : {'movies':horror_movies},
            'Adventure':{'movies':adv_movies},
            'Drama': {'movies':drama_movies},
            }
   
    # If you want to add more categories or pages, # add them to the dictionaries above.
    # The code below goes through the cats dictionary, then adds each category, # and then adds all the associated pages for that category.
    for cat, cat_data in cats.items():
#        c = add_cat(cat)
        c = add_cat(cat)
        for m in cat_data['movies']:
            add_movie(c, m)
    
    # Print out the categories we have added.
    for c in ClassifyModel.objects.all():
        for m in MovieModel.objects.filter(classify=c):
            print(f'- {c}: {m}')

def add_movie(cat,m):
    obj, created = MovieModel.objects.get_or_create(classify=cat, name=m["name"], defaults=m)
    return m
   
def add_cat(name):
    c = ClassifyModel.objects.get_or_create(name=name)[0]
    return c
        
    #Startexecutionhere!
if __name__=='__main__':
    print('Starting iCine population script...')
    populate()

