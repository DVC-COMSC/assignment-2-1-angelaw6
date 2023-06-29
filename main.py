def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    m_num = int(input("Enter the number of male students registered for this class: "))
    f_num = int(input('Enter the number of female students registered for this class: '))


    total = f_num + m_num
    f_perc = f_num *100 / total
    m_perc = m_num *100 / total

    print("The total number of students: \t %d" %(total))
    print("The number of males and females: \t %d \t %d" %(m_num, f_num))
    txt = ("The number of males and females: \t {male:.2f}% \t {female:.2f}*")
    print(txt.format(male = m_perc, female = f_perc))
    return  m_perc, f_perc


if __name__ == '__main__':
    main()
