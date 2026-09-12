/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eabushak <eabushak@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/20 14:14:48 by eabushak          #+#    #+#             */
/*   Updated: 2025/12/20 16:57:44 by eabushak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <unistd.h>
# include <stdarg.h>

int	ft_printf(const char *format, ...);
int	print_low_hex(unsigned int n);
int	print_up_hex(unsigned int n);
int	print_adress(unsigned long lo);
int	print_nbr(int n);
int	print_u(unsigned int n);
int	print_string(char *s);
int	print_char(int c);
int	handle_format(char spec, va_list *args);

#endif
