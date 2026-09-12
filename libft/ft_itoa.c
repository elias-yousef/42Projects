/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eabushak <eabushak@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/01 17:05:09 by eabushak          #+#    #+#             */
/*   Updated: 2025/12/13 11:22:17 by eabushak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	len(int n)
{
	int		i;
	long	nbr;

	nbr = n;
	i = 0;
	if (nbr <= 0)
	{
		nbr = nbr * -1;
		i++;
	}
	while (nbr > 0)
	{
		nbr /= 10;
		i++;
	}
	return (i);
}

static char	converting(long nbr)
{
	return (nbr % 10 + '0');
}

char	*ft_itoa(int n)
{
	char	*ptr;
	long	nbr;
	int		len_n;

	len_n = len(n);
	nbr = n;
	ptr = malloc(len_n + 1);
	if (ptr == NULL)
		return (NULL);
	ptr[len_n] = '\0';
	if (nbr < 0)
	{
		nbr *= -1;
		ptr[0] = '-';
	}
	if (nbr == 0)
		ptr[0] = '0';
	while (nbr > 0)
	{
		ptr[len_n - 1] = converting(nbr);
		nbr = nbr / 10;
		len_n--;
	}
	return (ptr);
}
