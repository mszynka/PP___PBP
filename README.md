# Równoważenie obciążenia przez alokację shardów



## Cykl życia przedsięwzięcia badawczego

1. Postawienie tezy
    1. Formalna definicja modelu, definicja zmiennych
2. Przeprowadzenie eksperymentu
    1. Budowa symulatora
    2. Przeprowadzenie eksperymentu
    3. Obróbka wyników
3. Analiza wyników
4. Publikacja

## Plan przedsięwzięcia

Chmura obliczeniowa – węzły są unikalne funkcjonalnie (inne usługi dostępu do danych, brak replikacji). Zarządzanie równomiernym obciążeniem poszczególnych węzłów. Strumień żądań dostępu (jednostka shard). Co zrobić żeby równoważyć obciążenie?
Założenie:
	- można dokonać predykcji obciążenia poszczególnych shardów.
Predykcja modelowana w postaci wektorów z przedziałami czasowymi, a wartościami są poziomy przewidywanego obciążenia w danej jednostce czasu. Optymalizacja ma polegać na takiej alokacji shardów, żeby obciążenie całego systemu było na stałym poziomie. Algorytm prealokacji zostanie przesłany później. Model ma przewidywać ilość shardów i podział ich na węzły chmury. Wartością badaną są opóźnienia.
Poziom obciążenia ma być zdefiniowany jako zmienna.