
## https://docs.python.org/3/howto/sorting.html
def sort_case_insensitive_preserve_case(input_phrase):
  print(sorted(input_phrase.split(), key=str.lower))

sort_case_insensitive_preserve_case("This is a test string from Andrew")
sort_case_insensitive_preserve_case("apple banana ORANGE")
sort_case_insensitive_preserve_case("apple ORANGE Banana ")