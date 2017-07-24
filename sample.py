from arff2pandas import a2p

if __name__ == '__main__':
    with open('sample.arff','r') as f:
        df = a2p.load(f)
        print(df)
    with open('sample.arff','w') as f:
        a2p.dump(df,f)