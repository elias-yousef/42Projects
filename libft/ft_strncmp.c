/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncmp.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eabushak <eabushak@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/26 20:19:07 by eabushak          #+#    #+#             */
/*   Updated: 2025/12/01 10:54:40 by eabushak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_strncmp(const char *s1, const char *s2, size_t n)
{
	unsigned const char	*ptr1;
	unsigned const char	*ptr2;
	size_t				i;

	ptr1 = (unsigned const char *)s1;
	ptr2 = (unsigned const char *)s2;
	i = 0;
	if (n == 0)
		return (0);
	while (i < n && ptr1[i] == ptr2[i] && ptr1[i] && ptr2[i])
		i++;
	if (n == i)
		return (0);
	return (ptr1[i] - ptr2[i]);
}
