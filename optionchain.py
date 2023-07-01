import requests
import json
import time

def printInTextCE(printText):
    txt = open("E:/Sidharth/CE.txt","a");
    txt.write(printText);
    txt.close();
def printInTextPE(printText):
    txt = open("E:/Sidharth/PE.txt","a");
    txt.write(printText);
    txt.close();

url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY";
head = {
    'accept':'*/*',
    'host':'www.nseindia.com',
    'accept-encoding':'gzip, deflate, br',
    'connection':'keep-alive',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

#res = requests.get(url=url,headers=head,timeout=10);
#print(type(str(res.json())));

#txt = open("E:/Sidharth/abcd.txt","w");
#txt.write(str(res.json()));
#txt.close();

expiryDateString = "13-Jul-2023";
minStrikePrice = 19000;
maxStrikePrice = 20000;
strikePriceDelta = 50;

sourceRawJson = open("E:/Sidharth/GitHub Repo/Stocks/sampleoptionchain.txt");
rawJson = sourceRawJson.read().replace("'",'"');
sourceRawJson.close();
sampleJson = json.loads(rawJson);
jsonString = json.loads(rawJson);

printInTextCE("Time\tCurrent Price\t");

#Column headers
strikePriceCounter = minStrikePrice;
while strikePriceCounter <= maxStrikePrice:
    printInTextCE(str(strikePriceCounter)+"\t");
    strikePriceCounter += strikePriceDelta;

for x in range(4):
    #Collect row data
    priceDict = {};
    priceDict['time'] = (str(jsonString['records']['timestamp'])).split()[1];
    priceDict['currentprice'] = str(jsonString['records']['underlyingValue']);

    for a in jsonString['records']['data']:
        if a['expiryDate']==expiryDateString:
            strikePrice = a['strikePrice'];
            priceDict[str(strikePrice)+"CE"] = a['CE']['lastPrice']

    #print row data
    printInTextCE("\n"+priceDict['time']+"\t"+priceDict['currentprice']);
    strikePriceCounter = minStrikePrice;
    while strikePriceCounter <= maxStrikePrice:
        printInTextCE("\t"+str(priceDict[str(strikePriceCounter)+"CE"]));
        strikePriceCounter += strikePriceDelta;
   


#for x in range(4):
 #   datas = "";

  #  for i in sampleJson['filtered']['data']:
   #     if (datas==""):
    #        datas = "\n"+i['expiryDate']+":"
     #   datas = datas+(str(i['strikePrice'])+","+str(i['CE']['lastPrice'])+","+str(i['PE']['lastPrice']))+";\n"

#print(datas);

    
    #time.sleep(1);



