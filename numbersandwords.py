#jc feb 23

def numsq(numbers):
        """this function squares the input number(s)

        Args: a list of number(s)

        returns: squares of numbers

        """

        sqlist = []
        for number in numbers:
                sqlist.append (number*number)
        return sqlist


def numsum(numbers):
        """this sums some numbers

        args: a list of number(s)

        returns: sum of said list
        """

        sumnums=0
        for number in numbers:
                sumnums= sumnums+number
        return sumnums


def shout_words(words):
        """ docs """
        shouts = [w.upper() + "!!" for w in words]
        return shouts




def main():
        """
                this makes it all work i guess
        """

        #handy list of numbers
        numbers = [3,8,5,7,3,6,9]
        #lkist of words
        words = ['Hello', 'Goodbye', 'Help']

        #call functino to add all numbers:
        sumnums = numsum(numbers)

        #call function to sqare nums
        sqnums = numsq(numbers)

        #do things with words
        shouts = shout_words(words)

        #print results:
        print "numlist is %s"  % str(numbers)
        print "sums is %s" % str(sumnums)
        print "sqares are %s" % str(sqnums)
        print "words are %s" % shouts


if __name__ == "__main__":
        main()
