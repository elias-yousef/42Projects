/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eabushak <eabushak@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/24 15:22:24 by eabushak          #+#    #+#             */
/*   Updated: 2025/12/01 11:07:00 by eabushak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strrchr(const char *s, int c)
{
	int		i;
	char	*ptr;

	ptr = NULL;
	i = 0;
	while (s[i] != '\0')
	{
		if (s[i] == (char )c)
			ptr = (char *)&s[i];
		i++;
	}
	if ((char )c == '\0')
		ptr = (char *)&s[i];
	return (ptr);
}
