class Int2Az:
    rank = [1, 10, 100, 1000, 1000000, 1000000000]
    ones = ['', 'bir ', 'iki ', 'üç ', 'dörd ', 'beş ', 'altı ', 'yeddi ', 'səkkiz ', 'doqquz ']
    tens = ['', 'on ', 'iyirmi ', 'otuz ', 'qırx ', 'əlli ', 'altmış ', 'yetmiş ', 'səksən ', 'doxsan ']

    @classmethod
    def _check_num(cls, num):
        if type(num) != int:
            raise Exception('Input number should be integer type.')

        if num > cls.rank[-1]:
            raise Exception('Input number should be lower than ' + str(cls.rank[-1]))

    @classmethod
    def _make_forstr(cls, a):
        i = 0
        forstr = []
        check = True
        while check != 0:
            num = a // cls.rank[i]
            if cls.rank[i] == 1:
                forstr.append(a % 10)
            elif cls.rank[i] == 100:
                forstr.append(num % 10)
            else:
                forstr.append(num % cls.rank[i])
            check = num != 0
            i += 1
        return(forstr)

    @classmethod
    def _forstr2str(cls, forstr):
        strnum = []
        for i, item in enumerate(forstr):
            item = int(item)
            if item != 0:
                if i == 0:
                    strnum.append(cls.ones[item])
                elif i == 1:
                    strnum.append(cls.tens[item])
                elif i == 2:
                    strnum.append(cls.ones[item] + 'yüz ')
                elif i == 3:
                    strnum.append(cls._forstr2str(cls._make_forstr(item)) + 'min ')
                elif i == 4:
                    strnum.append(cls._forstr2str(cls._make_forstr(item)) + 'milyon ')
        return ''.join(reversed(strnum))

    @classmethod
    def convert(cls, num):
        cls._check_num(num)
        return cls._forstr2str(cls._make_forstr(num)).strip()
