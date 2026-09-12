/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eabushak <eabushak@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/20 14:05:42 by eabushak          #+#    #+#             */
/*   Updated: 2025/12/20 17:24:54 by eabushak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	handle_format(char spec, va_list *args)
{
	if (spec == 'c')
		return (print_char((int )va_arg(*args, int)));
	else if (spec == 's')
		return (print_string((char *)va_arg(*args, char *)));
	else if (spec == 'd' || spec == 'i')
		return (print_nbr((int )va_arg(*args, int)));
	else if (spec == 'u')
		return (print_u((long )va_arg(*args, unsigned int)));
	else if (spec == 'p')
		return (print_adress((unsigned long )va_arg(*args, void *)));
	else if (spec == 'x')
		return (print_low_hex((unsigned int )va_arg(*args, unsigned int)));
	else if (spec == 'X')
		return (print_up_hex((unsigned int )va_arg(*args, unsigned int)));
	return (0);
}

int	ft_printf(const char *format, ...)
{
	va_list	args;
	int		count;

	count = 0;
	va_start(args, format);
	while (*format)
	{
		if (*format == '%')
		{
			if (*(format + 1) == '%')
				count += write(1, "%", 1);
			else
				count += handle_format(*(format + 1), &args);
			format += 2;
		}
		else
		{
			count += write(1, format, 1);
			format ++;
		}
	}
	va_end(args);
	return (count);
}
