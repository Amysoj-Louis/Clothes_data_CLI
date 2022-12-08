# Clothes_data_CLI

Hi, I have created an CLI that retrives data from Json file based on query
## Steps to use:
*Clone the repo.
*Go to the downloaded folder and open the cmmand prompt.
*Type `clothes --help` to see all commands


### Example 1

`clothes init -s "i want a red shirt" -f "testy" `


#Output
```
Found 884 product for "i want a red shirt" 
Found 13723 similar product for "i want a red shirt"
Your file has been saved at .../testy.json
```

### Example 2

`clothes idbased -s 15970`

#Output

```
{'id': 15970, 'gender': 'Men', 'masterCategory': 'Apparel', 'subCategory': 'Topwear', 'articleType': 'Shirts', 'baseColour': 'Navy Blue', 'season': 'Fall', 'year': 2011, 'usage': 'Casual', 'productDisplayName': 'Turtle Check Men Navy Blue Shirt', 'link': 'http://assets.myntassets.com/v1/images/style/properties/7a5b82d1372a7a5c6de67ae7a314fd91_images.jpg'}
```
