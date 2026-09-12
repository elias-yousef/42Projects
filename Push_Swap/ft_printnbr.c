/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printnbr.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mkhashan <mkhashan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/05 08:39:07 by mkhashan          #+#    #+#             */
/*   Updated: 2026/02/05 08:39:07 by mkhashan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_putnbr_fd(int n, int fd)
{
	long	nbr;
	char	c;

	nbr = n;
	if (nbr < 0)
	{
		write(fd, "-", 1);
		nbr = -nbr;
	}
	if (nbr >= 10)
	{
		ft_putnbr_fd(nbr / 10, fd);
	}
	c = (nbr % 10) + '0';
	write(fd, &c, 1);
}

int	ft_printnbr(int nbr)
{
	int	count;

	if (nbr == -2147483648)
	{
		return (write(2, "-2147483648", 11));
	}
	if (nbr == 0)
	{
		return (write(2, "0", 1));
	}
	count = 0;
	ft_putnbr_fd(nbr, 2);
	if (nbr < 0)
	{
		count += 1;
		nbr *= -1;
	}
	while (nbr > 0)
	{
		nbr /= 10;
		count += 1;
	}
	return (count);
}
