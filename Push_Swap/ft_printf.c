/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mkhashan <mkhashan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/05 08:34:24 by mkhashan          #+#    #+#             */
/*   Updated: 2026/02/05 08:34:24 by mkhashan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	type_handlor(va_list arg, char conversion)
{
	int	size;

	size = 0;
	if (conversion == 'i' || conversion == 'd')
		size = ft_printnbr(va_arg(arg, int));
	else if (conversion == 'f')
		size = ft_printfloat(va_arg(arg, double));
	else if (conversion == 's')
		size = ft_printstr(va_arg(arg, char *));
	else if (conversion == '%')
		size = write(2, "%", 1);
	else
		size = write(2, "%", 1) + write(2, &conversion, 1);
	return (size);
}

int	ft_printf(const char *format, ...)
{
	va_list	arg;
	int		i;
	int		count;

	i = 0;
	count = 0;
	va_start(arg, format);
	while (format[i])
	{
		if (format[i] == '%')
		{
			if (format[i + 1] == '\0')
			{
				va_end(arg);
				return (-1);
			}
			i++;
			count += type_handlor(arg, format[i]);
		}
		else
			count += write(2, &format[i], 1);
		i++;
	}
	va_end(arg);
	return (count);
}
