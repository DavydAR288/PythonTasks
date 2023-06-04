import view
import database


def main():
    while True:
        ask = view.user_input()

        if ask == 0:
            database.delete_data()
        elif ask == 1:
            quest = view.input_data()
            database.write_data(quest)
        elif ask == 2:
            quest = view.input_search()
            database.search_data(quest)
        elif ask == 3:
            database.sort_data()
        elif ask == 4:
            database.view_families()
        elif ask == 5:
            database.view_all()
        elif ask == 6:
            quest = view.input_correct()
            if database.correct(quest)==True:
                quest = view.input_data()
                database.write_data(quest)
        elif ask == 7:
            quest = view.input_delete()
            database.delete(quest)
        elif ask == 8:
            return False


main()
