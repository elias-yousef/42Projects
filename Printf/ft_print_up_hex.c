/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_up_hex.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eabushak <eabushak@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/20 14:50:32 by eabushak          #+#    #+#             */
/*   Updated: 2025/12/20 16:30:55 by eabushak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

static int	convtohexup(unsigned long lo)
{
	char	chr;

	if (lo % 16 == 10)
		write(1, "A", 1);
	else if (lo % 16 == 11)
		write(1, "B", 1);
	else if (lo % 16 == 12)
		write(1, "C", 1);
	else if (lo % 16 == 13)
		write(1, "D", 1);
	else if (lo % 16 == 14)
		write(1, "E", 1);
	else if (lo % 16 == 15)
		write(1, "F", 1);
	else
	{
		chr = lo % 16 + '0';
		write(1, &chr, 1);
	}
	return (1);
}

int	print_up_hex(unsigned int n)
{
	int	counter;

	counter = 0;
	if (n >= 16)
	{
		counter += print_up_hex(n / 16);
		counter += convtohexup(n);
	}
	else
	{
		counter += convtohexup(n);
	}
	return (counter);
}
