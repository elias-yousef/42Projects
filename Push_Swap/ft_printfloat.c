/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printfloat.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mkhashan <mkhashan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/05 08:42:06 by mkhashan          #+#    #+#             */
/*   Updated: 2026/02/05 08:42:06 by mkhashan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	ft_printfloat(double nbr)
{
	int	integer_part;
	int	decimal_part;

	if (nbr < 0)
	{
		write(2, "-", 1);
		nbr = -nbr;
	}
	integer_part = (int)nbr;
	decimal_part = (int)((nbr - integer_part) * 100);
	ft_printnbr(integer_part);
	write(2, ".", 1);
	if (decimal_part < 10)
		write(2, "0", 1);
	ft_printnbr(decimal_part);
	return (1);
}
