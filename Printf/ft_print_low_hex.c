/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_low_hex.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eabushak <eabushak@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/20 14:49:04 by eabushak          #+#    #+#             */
/*   Updated: 2025/12/20 16:30:01 by eabushak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static int	convtohex(unsigned long lo)
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

int	print_low_hex(unsigned int n)
{
	int	counter;

	counter = 0;
	if (n >= 16)
	{
		counter += print_low_hex(n / 16);
		counter += convtohex(n);
	}
	else
	{
		counter += convtohex(n);
	}
	return (counter);
}
