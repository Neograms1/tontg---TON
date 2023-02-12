import requests


token = "Введите свой токен"

class Pay():
    
    
    def __init__(self,token):
        self.token = token
    
    def pay_link(self,amount,description = None ):
        """Функция создана что бы получать URL ссылки для опалаты"""
        
        url = 'https://pay.crypt.bot/api/createInvoice'
        headers = {'Crypto-Pay-API-Token' : self.token}
        params = {'asset' : 'TON',
                  'amount' : amount,
                  'description' : description}
        req = requests.get(url,headers=headers,params=params)
        link =  req.json()['result']['pay_url']
        self.ids = req.json()['result']['invoice_id']
        return link
    
    
    
    def check(self):
        ''' Проверяет активный  текущий чек
        Это функция не может быть вызвана если не вызвана функция pay()
        '''
        
        headers = {'Crypto-Pay-API-Token' : self.token}
        urls = 'https://pay.crypt.bot/api/getInvoices'
        reqs = requests.get(urls,headers=headers,params={'invoice_ids' : self.ids})
        dins = reqs.json()['result']['items'][0]['status']
        return dins
    
    def balance(self):
        'Функция balance что бы получить баланас'
        headers = {'Crypto-Pay-API-Token' : self.token}
        url_balance = 'https://pay.crypt.bot/api/getBalance'
        reqs = requests.get(url_balance,headers=headers).json()
        return(reqs['result'][1]['available'])
      


bot  = Pay(token) #принимает только один параметер token 


print(bot.pay_link(amount = 1))  # что бы получить сссылку 
print(bot.check()) # что бы получить активный ли статус или нет
print(bot.balance()) # что бы получить баланас
