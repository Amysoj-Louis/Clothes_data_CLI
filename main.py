import click
import json
import os
with open('data.json', 'r') as f:
    data = json.load(f)


@click.group()
def ecloth():
    pass


@ecloth.command()
@click.option("--count", "-c", default=1, help="Number of Results.")
@click.option("--search", "-s", prompt="Hello, please enter your Query", help="The Query to search.")
@click.option("--file", "-f", prompt="Please enter file name", help="The name of file.")
def init(count, search, file):
    """Simple program that gets Clothes data based on the query for a total of COUNT times."""
    myOutput, Query = [], []
    HighScore = 1
    Input = search.lower()
    for word in Input.split():
        if len(word) >= 3:
            if Input.count(word) == 1:
                Query.append(word)
            else:
                pass
    try:
        for j in data:
            Score = 0
            for i in Query:
                if i in j['articleType'].lower():
                    Score += 1
                if i in j['baseColour'].lower():
                    Score += 1
                if i in j['gender'].lower():
                    Score += 1
                if i in j['masterCategory'].lower():
                    Score += 1
                if i in j['subCategory'].lower():
                    Score += 1
                if i in j['season'].lower():
                    Score += 1
                if i in j['usage'].lower():
                    Score += 1
                pid = {"ID": f"{j['id']}", "SCORE": Score, "FULL_DATA": j}
                if Score >= 1:
                    if Score >= HighScore:
                        HighScore = Score
                    myOutput.append(pid)
        myOutput = sorted(
            myOutput, key=lambda d: d['SCORE'], reverse=True)
        Output, Similar = [], []
        Output = [x
                  for x in myOutput if x["SCORE"] >= HighScore]
        Similar = [x
                   for x in myOutput if x["SCORE"] < HighScore]
        print(f'Found {len(Output)} product for "{Input}"')
        print(
            f'Found {len(Similar)} similar product for "{Input}"')
        mydata = {"data": [{"mostMatched": Output, "similarResult": Similar}]}
        with open(f'{file}.json', 'w') as f:
            json.dump(mydata, f)
        dir_path = os.path.dirname(os.path.realpath(__file__))
        print(f" Your file has been saved at {dir_path+'/'+file}.json")
    except Exception as e:
        print(e)


@ecloth.command()
@click.option("--id", "-s", type=int, prompt="Hello, please enter your Query", help="The Query to search.")
def idbased(id):
    """Get data from json using id"""
    gotid = False
    for j in data:
        if id == j['id']:
            print(j)
            gotid = True
    if gotid == False:
        print("The id doesn't exist")


if __name__ == "__main__":
    ecloth()
