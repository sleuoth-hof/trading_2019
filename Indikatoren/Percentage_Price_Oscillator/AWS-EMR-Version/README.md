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

*Note: Alternativly Datasources can be used (i.e. this git's 'Interpolierte-Daten') - Paths may need to be adjusted.*
 
```
git clone https://github.com/sleuoth-hof/trading_2019.git;
echo "Paths may need to be adjusted:";
cd trading_2019/Interpolation/;
echo "Source-Structure may need to be adjusted:"
unzip interpolierte\ Daten.zip .;
cd Kollekt;
echo "This might been already fixed:";
rm udcusd\ -\ Kopie.csv
cd ~;
mkdir ABDA2019/testdaten/;
mv trading_2019/Interpolation/Kollekt ABDA2019/testdaten/cryptominuteresolution;
hdfs dfs -put ABDA2019 .;
```

#### All-Nodes:
```
wget https://bootstrap.pypa.io/get-pip.py;
sudo python get-pip.py;
sudo yum -y install numpy;
```


INSTRUCTIONS
---

#### Skript-Preparation:

*Note: PY-Skripts are located '~/trading_2019/Indikatoren/Percentage_Price_Oscillator/AWS-EMR-Version/', when this git is cloned:*
```
cd ~;
mv trading_2019/Indikatoren/Percentage_Price_Oscillator/AWS-EMR-Version/PPO_Indikator_1.py ppo1.py;
mv trading_2019/Indikatoren/Percentage_Price_Oscillator/AWS-EMR-Version/PPO_Indikator_2.py ppo2.py;
```

#### Main-Skript:
```
spark-submit --deploy-mode cluster  --master yarn  ppo1.py;
cd ~;
if [ ! -d tmp_warehouse ]
then
mkdir tmp_warehouse
fi
hdfs dfs -get tmp_warehouse/dataframe tmp_warehouse/dataframe;
cd tmp_warehouse;
cd dataframe;
cat part-*.csv >> ~/tmp_warehouse/dataframe.csv;
cd ..;
rm -R dataframe;
cd ..;
hdfs dfs -put ./tmp_warehouse/dataframe.csv tmp_warehouse;
spark-submit --deploy-mode cluster  --master yarn  ppo2.py;
hdfs dfs -get warehouse warehouse;
cd ~;
cd warehouse;
for dir in */
do
cd "$dir"
if [ -f ~/warehouse/"${dir::-1}".csv ]
then
rm ~/warehouse/"${dir::-1}".csv
fi
awk '(NR == 1) || (FNR > 1)' part-*.csv > ~/warehouse/"${dir::-1}".csv
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
scp -i key_file.pem hadoop@{aws_emr_master}:~/warehouse.zip .;
```
