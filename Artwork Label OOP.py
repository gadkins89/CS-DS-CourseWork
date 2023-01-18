#9.13 Lab: Artwork Label (Classes / Constructors)



class Artist:

    def __init__(self, name="Unknown", birth_year=-1, death_year=-1):
        self.name = name
        self.birth_year = birth_year
        self.death_year = death_year

    def print_artist_info(self):
        if self.birth_year and self.death_year > 0:
            print(f"Artist: {self.name}, ({self.birth_year} to {self.death_year}) \n")
        elif self.birth_year > 0 and self.death_year < 0:
            print(f"Artist: {self.name}, ({self.birth_year} to Present) \n")
        else:
            print(f"Artist: {self.name}, (Unknown) \n")

class Artwork:

    def __init__(self, title="Unknown", year_created=-1, artist=Artist):
        self.title = title
        self.year_created = year_created
        self.artist = artist

    def print_work_info(self):
        print(f"Title: {self.title}, {self.year_created} \n")

if __name__ == "__main__":
    user_artist_name = input("What is the name of the Artist? \n")
    user_birth_year = int(input("What is the birth year of the artist? \n"))
    user_death_year = int(input("What is the death year of the artist? \n"))
    user_title = input("What is the title of the work? \n")
    user_year_created = int(input("What is the year the work was created? \n"))

    user_artist = Artist(user_artist_name, user_birth_year, user_death_year)

    new_artwork = Artwork(user_title, user_year_created, user_artist)
  
    user_artist.print_artist_info()
    
    new_artwork.print_work_info()