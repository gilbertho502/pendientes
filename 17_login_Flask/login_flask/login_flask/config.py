class Config(object):

    #conectando con postgress
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:cargamos2022@localhost:5432/bdcargamos'
    #SQLALCHEMY_DATABASE_URI = 'postgresql://kgtafqvflvyqxy:1b17284863c92c3696de9bb5bb30142a9540cb24f738e0b1abcccb9042d1eb5b@ec2-52-0-114-209.compute-1.amazonaws.com:5432/ddb638dq9if2os'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
