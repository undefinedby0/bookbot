def main():
  with open("books/frankenstein.txt") as f:
    letter_counts = {}
    
    file_contents = f.read()
    lowercase_text = file_contents.lower()
    words = file_contents.split()
    
    for char in lowercase_text.lower():
      if char in letter_counts:
        letter_counts[char] += 1
      else:
        letter_counts[char] = 1
    
    
    
    letter_counts_list = convert_dict_to_list_of_dicts(letter_counts)
    letter_counts_list.sort(reverse=True, key=sort_on)
    
    
    print(f"--- Begin report of {f.name} ---")
    print(f"{len(words)} words found in the document\n")
    for obj in letter_counts_list:
      if obj["char"].isalpha():
        print(f"The '{obj["char"]}' character was found {obj["num"]} times")
    
    print(f"--- End report ---")
    
def convert_dict_to_list_of_dicts(dict):
  return [{"char": key, "num": value} for key, value in dict.items()]
    
def sort_on(dict):
  return dict["num"]
    
    
if __name__ == '__main__':
  main()
  