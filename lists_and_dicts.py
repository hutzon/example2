def run():
    my_list = [1, "Hola", 2.5]
    my_dict = {"firstname":"Ottoniel", "lastname": "Campos"}

    super_list = [
        {"firstname":"Ottoniel", "lastname": "Campos"},
        {"firstname":"Cristian", "lastname": "Campos"},
        {"firstname":"Kandy", "lastname": "Ramos"},
        {"firstname":"Walter", "lastname": "Caceres"},
        {"firstname":"Noe", "lastname": "Herrera"},
        {"firstname":"Daniel", "lastname": "Morales"}  ,    
    ]

    super_dict = {
        "natural_nums":[1,2,3,4,5],
        "integer_nums":[-1,-2,0,1,2],
        "floating_nums":[2.3, 4.6, 2.65],
    }

    for key, value in super_dict.items():
        print(key, "_",value)


if __name__ == "__main__":
    run()
