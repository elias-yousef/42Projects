
NAME = push_swap
CC = cc
CFLAGS = -Wall -Wextra -Werror

SRCS = push_swap.c atoi.c bench.c Complex_sort.c compute_disorder.c ft_printf.c ft_printfloat.c ft_printnbr.c ft_printstr.c ft_strncmp.c les5_sort.c \
		Medium_sort.c ops1.c ops2.c ops3.c repair_sort.c Simple_sort.c sort.c utils.c

OBJS = $(SRCS:.c=.o)

all: $(NAME)

$(NAME): $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $(NAME)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS)
fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re