class colors:
    cyan = "\033[1;36m"     # Ciano
    red = "\033[91m"        # Vermelho
    green = "\033[92m"      # Verde brilhante
    yellow = "\033[93m"     # Amarelo
    blue = "\033[94m"       # Azul brilhante
    magenta = "\033[95m"    # Magenta
    dark_green = "\033[32m" # Verde escuro
    dark_blue = "\033[34m"  # Azul escuro
    light_green = "\033[1;92m"  # Verde claro
    light_blue = "\033[1;94m"   # Azul claro
    end = "\033[0m"          # Reset para a cor padrão
    


class forma:
	neg =  "\033[1m" #texto mais espesso
	sub =  "\033[4m" #linha embaixo do texto
	inver = "\033[7m" #inversao de cores
	neg_b =  "\033[1m"    #Bright
	escuro =  "\033[2m" #escuro
	i =  "\033[3m" #(nem todos os terminais suportam)
	double_s = "\033[21m"
	pisc = "\033[5m" #(nem todos os terminais suportam)
	speed_text = "\033[6m"
	hidden_text =  "\033[8m"
	end = "\033[0m"
	
#("\033[31mTexto em vermelho\033[0m")
#("\033[1;32mTexto em verde e em negrito\033[0m")
#(forma.hidden_text+"testeste"+colors.end)
#(forma.speed_text+"rapido"+colors.end)
#(forma.Piscante+"pisca pisca"+colors.end)