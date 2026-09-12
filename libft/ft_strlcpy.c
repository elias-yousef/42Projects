/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eabushak <eabushak@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/26 14:43:30 by eabushak          #+#    #+#             */
/*   Updated: 2025/12/01 10:21:48 by eabushak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlcpy(char *dst, const char *src, size_t size)
{
	size_t	c;
	size_t	count;

	count = 0;
	while (src[count])
		count++;
	if (size == 0)
		return (count);
	c = 0;
	while (c < size - 1 && src[c])
	{
		dst[c] = src[c];
		c++;
	}
	dst[c] = '\0';
	return (count);
}
