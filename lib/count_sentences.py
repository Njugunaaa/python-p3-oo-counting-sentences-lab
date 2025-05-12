#!/usr/bin/env python3

class MyString:
  def __init__(self,value=""):
      self.value=value

  def get_value(self):
      return self._value
  
  def set_value(self, value):
        if isinstance(value, str) :
            self._value = value
        else:
            print("The value must be a string.")
  value = property(get_value, set_value)

  def is_sentence(self):
      return self.value.endswith(".")
  def is_question(self):
      return self.value.endswith("?")

  def is_exclamation(self):
      return self.value.endswith("!")
    
  def count_sentences(self):
    replaced = self.value.replace("!", ".").replace("?", ".")
    parts = replaced.split(".")
    sentences = [s for s in parts if s.strip()]
    return len(sentences)
