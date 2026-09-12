/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_adress.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eabushak <eabushak@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/20 14:51:40 by eabushak          #+#    #+#             */
/*   Updated: 2025/12/20 17:06:28 by eabushak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	convtohex(unsigned long lo)
{
	char	chr;

	if (lo % 16 == 10)
		write(1, "a", 1);
	else if (lo % 16 == 11)
		write(1, "b", 1);
	else if (lo % 16 == 12)
		write(1, "c", 1);
	else if (lo % 16 == 13)
		write(1, "d", 1);
	else if (lo % 16 == 14)
		write(1, "e", 1);
	else if (lo % 16 == 15)
		write(1, "f", 1);
	else
	{
		chr = lo % 16 + '0';
		write(1, &chr, 1);
	}
	return (1);
}

int	print_adress(unsigned long lo)
{
	int	counter;

	counter = 0;
	if (lo == 0)
	{
		write(1, "(nil)", 5);
		return (5);
	}
	if (lo >= 16)
	{
		counter += print_adress(lo / 16);
		counter += convtohex(lo);
	}
	else
	{
		write(1, "0x", 2);
		counter += convtohex(lo) + 2;
	}
	return (counter);
}
