---
Requierments
---
- AWS-EMR-Enviorment with Hadoop and Spark
- File `~/ppo1.py` (name can be adjusted)
- File `~/ppo2.py` (name can be adjusted)
---

SETUP
---

#### Master:
```
cd ~;
sudo yum -y install git;
git clone https://github.com/sleuoth/ABDA2019.git;
cd ABDA2019/testdaten/cryptominuteresolution;
unzip btcusd.csv.zip .;
rm btcusd.csv.zip;
cd ~;
hdfs dfs -put ABDA2019 ABDA2019;
```

#### All-Nodes:
```
wget https://bootstrap.pypa.io/get-pip.py;
sudo python get-pip.py;
sudo yum -y install numpy;
```


INSTRUCTIONS
---

#### Main-Skript:
```
spark-submit --deploy-mode cluster  --master yarn  ppo1.py;
cd ~;
if [ ! -d tmp_warehouse ]
then
mkdir tmp_warehouse
fi
hadoop dfs -get tmp_warehouse/dataframe tmp_warehouse/dataframe;
cd tmp_warehouse;
cd dataframe;
cat part-*.csv >> ~/tmp_warehouse/dataframe.csv;
cd ..;
rm -R dataframe;
cd ..;
hdfs dfs -put ./tmp_warehouse/dataframe.csv tmp_warehouse;
spark-submit --deploy-mode cluster  --master yarn  ppo2.py;
hadoop dfs -get warehouse warehouse;
cd ~;
cd warehouse;
for dir in */ 
do
cd "$dir"
if [ -f ~/warehouse/"${dir::-1}".csv ]
then
rm ~/warehouse/"${dir::-1}".csv
fi
cat part-*.csv >> ~/warehouse/"${dir::-1}".csv
cd ..
rm -R "$dir"
done;
cd ..;
```

DOWNLOAD
---
```
cd ~;
zip -r warehouse.zip warehouse;
scp -i key_file.pem hadoop@{aws_emr_master}:~/warehouse.zip .
```
