class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if len(title.strip())==0:
            raise RuntimeError()
        self._title = title
    
    @property
    def isbn(self):
        return self._isbn
    
    @isbn.setter
    def isbn(self, isbn):
        digits = [int(digit) for digit in isbn.replace("-","")]
        digits = [digit*3 if index%2!=0 else digit for index, digit in enumerate(digits)]
        if len(digits)==13 and sum(digits)%10==0:
            self._isbn = isbn
        else:
            raise RuntimeError()