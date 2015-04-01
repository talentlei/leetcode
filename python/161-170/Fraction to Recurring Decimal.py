    def fractionToDecimal(self, numerator, denominator):
        if denominator==0:
            return None
        if numerator==0:
            return '0'
        flag=''
        if (numerator>0 and denominator<0 ) or (numerator <0 and denominator>0):
            flag='-'
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        head=numerator//denominator
        re =numerator%denominator 
        if re==0:
            return flag+str(head)
            
        counter=0
        Dic={}
        Dic[re]=counter
        counter+=1
        
        tail=''
        pbeg=-1
        while True:
            re*=10
            tail+=str(re/denominator)
            if re%denominator==0:
                break
            re=re%denominator
            if re in Dic:
                pbeg=Dic[re]
                break
            else:
                Dic[re]=counter
                counter+=1
        if pbeg==-1:
            return flag+str(head)+'.'+tail
        return flag+str(head)+'.'+tail[:pbeg]+'('+tail[pbeg:]+')'
