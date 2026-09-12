/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_nbr.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eabushak <eabushak@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/20 14:55:35 by eabushak          #+#    #+#             */
/*   Updated: 2025/12/20 16:45:31 by eabushak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	print_nbr(int n)
{
	int		counter;
	char	chr;
	long	nb;

	nb = (long )n;
	counter = 0;
	if (nb < 0)
	{
		counter += write(1, "-", 1);
		nb = -nb;
	}
	if (nb >= 10)
	{
		counter += print_nbr(nb / 10);
		chr = nb % 10 + '0';
		counter += write(1, &chr, 1);
	}
	else if (nb < 10 && nb >= 0)
	{
		chr = nb + '0';
		counter += write(1, &chr, 1);
	}
	return (counter);
}
