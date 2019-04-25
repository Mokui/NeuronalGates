# coding: utf-8


def mean(tab):
    try:
        val = 0
        tot = 0
        for k in tab:
            val+=k
            tot+=1
        return val/tot
    except ZeroDivisionError:
        print("You can't divide by 0.")
    except Exception as e:
        print(f"You fail the mean, error: {str(e)}.")