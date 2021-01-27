# def searcher():
#     import time
#     # Some 4 seconds time consuming task
#     book = "This is a book on harry and code with harry and good"
#     time.sleep(4)
#
#     while True:
#         text = (yield)
#         if text in book:
#             print("Your text is in the book")
#         else:
#             print("Text is not in the book")
#
# search = searcher()
# print("search started")
# next(search)
# print("Next method run")
# search.send("harry")
#
# search.close()
# search.send("harry")

# input("press any key")
# search.send("harry and")
# input("press any key")
# search.send("thi si")
# input("press any key")
# search.send("joker")
# input("press any key")
# search.send("like this video")

#-------------------------------------------CHALLENGE ACCEPTED----------------------------------------------------------

def search_assisatant():
    import time
    Book = "Salil , Ujjwal , Nikhil , Golu , Shrija , Sameer , Shashank , Prathamesh"
    print("Searching...")
    time.sleep(3)

    while True:
        text = (yield)
        if text in Book:
            print("Congradulation , Your name is in their List...")
        else:
            print("Sorry , We can't able to find your name in the List...")

search = search_assisatant()
next(search)
search.send("Shrija")


search = search_assisatant()
next(search)
search.send("Shalaka")
search.close()




