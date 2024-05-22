# Gra Flappy Bird z AI za pomocą NEAT

## Opis

Ten projekt to implementacja klasyka gier Flappy Bird przy użyciu Pythona i Pygame, rozszerzona o możliwości sztucznej inteligencji (AI) dostarczane przez bibliotekę NeuroEvolution of Augmenting Topologies (NEAT). Gra zawiera ptaka, który musi przefrunąć pomiędzy poruszającymi się kolumnami bez ich dotykania. AI uczy się, jak grać w grę, poprawiając swoje wydajność na przestrzeni czasu, na podstawie funkcji dopasowania zdefiniowanej podczas procesu ewolucji.

Gra pierwotnie została opracowana przy użyciu modułu Arcade do szkolenia AI, ale ze względu na problemy z architekturą i błędy podczas implementacji, przeniesiona została na Pygame dla lepszego sterowania i kompatybilności.

## Wymagania

Aby uruchomić tę grę, potrzebujesz:

- Zainstalowanego Pythona na Twoim systemie.
- Zainstalowanego Pygame. Możesz go zainstalować za pomocą `pip install pygame`


- Zainstalowanego NEAT-Python. Ta biblioteka jest używana do ewolucji sieci neuronowych. Zainstaluj ją za pomocą `pip install neat-python`

## Jak uruchomić grę
1. Upewnij się, że masz zainstalowany Python, Pygame oraz NEAT-Python na swoim systemie.
2. Mozliwość zmieniania parametrów sieci `NEAT` w pliku konfiguracyjnym `config-feedforward.txt`. Ten plik zawiera wszystkie parametry, które mogą być dostosowane do indywidualnych potrzeb:
   - `pop_size`: Określa liczbę osobników (ptaków) w populacji, którzy będą uczestniczyć w procesie ewolucji. Zwiększenie tej wartości może przyspieszyć proces uczenia, ale również zwiększy obliczeniowe koszty.
   - `fitness_threshold`: Ustala minimalną wartość fitness, którą musi osiągnąć organizm, aby móc przetrwać do kolejnego pokolenia. Zmniejszenie tego progu może przyspieszyć ewolucję, ale ryzykuje utratą zdobytej do tej pory wiedzy.
   - `bias`: Parametry związane z biasem w sieciach neuronowych, takie jak `bias_init_mean`, `bias_init_stdev`, `bias_max_value`, `bias_min_value`, `bias_mutate_power`, `bias_mutate_rate`, i `bias_replace_rate`. Dostosowanie tych wartości pozwala na modyfikację sposobu, w jaki sieć uczy się reprezentować dane wejściowe i wyjściowe.

3. Wykonaj skrypt `python main.py` z ścieżką do pliku konfiguracyjnego jako argument:


##

 Wzorowano się na tym projekcie [link](https://www.youtube.com/watch?v=MMxFDaIOHsE&list=PLzMcBGfZo4-lwGZWXz5Qgta_YNX3_vLS2&ab_channel=TechWithTim)
