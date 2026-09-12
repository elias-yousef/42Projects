# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: eabushak <eabushak@learner.42.tech>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/06 17:19:11 by eabushak          #+#    #+#              #
#    Updated: 2025/12/20 18:01:42 by eabushak         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME	= libftprintf.a

CC		= cc
CFLAGS	= -Wall -Wextra -Werror

AR		= ar rcs
RM		= rm -f

SRCS	= ft_printf.c \
		  ft_print_adress.c \
		  ft_print_char.c \
		  ft_print_string.c \
		  ft_print_nbr.c \
		  ft_print_uint.c \
		  ft_print_low_hex.c \
		  ft_print_up_hex.c

OBJS	= $(SRCS:.c=.o)

all: $(NAME)

$(NAME): $(OBJS)
	$(AR) $(NAME) $(OBJS)

%.o: %.c ft_printf.h
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	$(RM) $(OBJS)

fclean: clean
	$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean re
