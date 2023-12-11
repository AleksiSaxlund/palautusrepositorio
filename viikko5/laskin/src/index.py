from tkinter import Tk
from kayttoliittyma import Kayttoliittyma
from sovelluslogiikka import Sovelluslogiikka


def main():
    sovellus = Sovelluslogiikka()

    window = Tk()
    window.title("Laskin")

    kayttoliittyma = Kayttoliittyma(sovellus, window)
    kayttoliittyma.kaynnista()

    window.mainloop()

if __name__ == "__main__":
    main()
def get_all_references_by_user_id(self, user_id):
        """Returns all citations by the given user id."""
        references = Reference.query.join(UserReferences_model,
                                                UserReferences_model.reference_id
                                                == Reference.id).\
                                                    filter(UserReferences_model.user_id == user_id,
                                                           Reference.visible.is_(True)).all()