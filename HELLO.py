import pandas
df = pandas.read_csv("./mmm.csv")
df["serie_name"] = df["serie"].apply(lambda x: x.split("_")[1])
bb = df[["scale", "serie_name"]].groupby("serie_name").agg(list).reset_index()
bb["scale"] = bb["scale"].apply(lambda x: ','.join(list(set(x))))
bb.to_csv("./fff.csv", index=False, encoding="utf-8-sig")
print("nn")