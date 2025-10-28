print('This is your BOOK!!!')
shelf, wants = input('Enter input: ').split('/')
shelf, wants = shelf.split(' '), wants.split(' ')
payment = 0

def find_book(shelf, wants):
    global payment
    count = 0
    counter = []
    for wanted_books in wants:
        
        if wanted_books in shelf:
            for books in shelf:
                if wanted_books == books:
                    temp = shelf[:]
                    temp.pop(count)
                    shelf = [wanted_books] + temp
                    print(f'Search {wanted_books} -> found at {count+1} move to front ->  {" ".join(shelf)}')
                    payment += count+1
                    count = 0
                    break
                else:
                    count+= 1
                    
        elif wanted_books in counter:
            for books in counter:
                if wanted_books == books:
                    shelf = [wanted_books] + shelf
                    print(f'Search {wanted_books} -> add new book ->  {" ".join(shelf)}')
                    payment += 1
                    counter.pop(count)
                    count = 0
                    break
                else:
                    count+= 1
                
        else:
            print(f'Search {wanted_books} -> not found -> {" ".join(shelf)}')
            payment += len(shelf)+1
            counter.append(wanted_books)
    return shelf

shelf = find_book(shelf, wants)
print(f'\nFinal books: {" ".join(shelf)}\nTotal cost: {payment}')
