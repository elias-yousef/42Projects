/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_uint.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eabushak <eabushak@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/20 15:00:30 by eabushak          #+#    #+#             */
/*   Updated: 2025/12/20 16:34:32 by eabushak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	print_u(unsigned int n)
{
	int		counter;
	char	chr;

	counter = 0;
	if (n >= 10)
	{
		counter += print_u(n / 10);
		chr = n % 10 + '0';
		counter += write(1, &chr, 1);
	}
	else if (n < 10)
	{
		chr = n + '0';
		counter += write(1, &chr, 1);
	}
	return (counter);
}
