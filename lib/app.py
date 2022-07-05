from .api import fetch_repos
from .repo import Repo

class CLI():

    def __init__(self):
        self._user_input = ""

    def start(self):
        print(f'Repos are Coming...\n')
        fetch_repos()
        self.menu()

    def menu(self):
        for idx, repo in enumerate(Repo.all, start=1):
            print(f'{idx}. {repo.name}')
        self.get_user_choice()

    def get_user_choice(self):
        try:
            self._user_input = input(f'Which repo would you like see more info for?\n')
            if self._user_input == 'exit':
                return self.goodbye()
            if not self.valid_input(self._user_input):
                raise ValueError
            self.show_repo()
            self.get_user_choice()
        except ValueError:
            print('not a valid input')
            self.menu()

    def show_repo(self):
        repo = Repo.find_by_input(self._user_input)
        print(f'\nStargazers: {repo._stargazers}')
        print(f'\nForks: {repo.forks}')

    @staticmethod
    def valid_input(i):
        return int(i)>0 and int(i) <= len(Repo.all)
    
    @staticmethod
    def goodbye():
        print(f'\nbye.\n')

if __name__ == '__main__':
    app = CLI()
    