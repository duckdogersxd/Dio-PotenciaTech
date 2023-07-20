  def main():
    n = int(input())
 
    total = 0
 
    for i in range(1, n + 1):
        pedido = input().split(" ")
        nome = pedido[0]
        valor = float(pedido[1])
        total += valor
    desconto = input()
    
    desconto = getDescont(desconto)
    
    total *= desconto

    
    print(f'Valor total: {total:.2f}')
 
def getDescont(desconto):
  return 1-(int(desconto[0:-1])/100)
 
 
if __name__ == "__main__":
    main()
