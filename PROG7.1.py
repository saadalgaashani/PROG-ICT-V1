def hoogvliegers(dict_studenten_cijfers):


    student_cijfer_0pslag ={}
    for naam,cijfer in dict_studenten_cijfers.items():
        if cijfer >9.0:
            print(naam,"=",cijfer)
    return student_cijfer_0pslag



hoogvliegers({"saad":3,"jurjan":5,"melle":9.3,"aymen":9.9})