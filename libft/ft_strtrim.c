/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eabushak <eabushak@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/05 09:34:22 by eabushak          #+#    #+#             */
/*   Updated: 2025/12/13 10:32:11 by eabushak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static size_t	countstart(char const *s1, char const *set)
{
	size_t	i;
	size_t	j;

	i = 0;
	while (s1[i] != '\0')
	{
		j = 0;
		while (set[j] != '\0' && s1[i] != set[j])
			j++;
		if (!set[j])
			break ;
		i++;
	}
	return (i);
}

static size_t	countend(char const *s1, char const *set)
{
	size_t	i;
	size_t	j;

	if (!s1[0])
		return (0);
	i = ft_strlen(s1) - 1;
	while (1)
	{
		j = 0;
		while (set[j] && s1[i] != set[j])
			j++;
		if (!set[j])
			break ;
		if (i == 0)
			return (ft_strlen(s1));
		i--;
	}
	return (ft_strlen(s1) - i - 1);
}

static char	*trim_alloc(char const *s1, size_t start, size_t end, size_t len)
{
	char	*ptr;
	size_t	i;

	if (start + end >= len)
	{
		ptr = malloc(1);
		if (!ptr)
			return (NULL);
		ptr[0] = '\0';
		return (ptr);
	}
	ptr = malloc(len - start - end + 1);
	if (!ptr)
		return (NULL);
	i = 0;
	while (i < len - start - end)
	{
		ptr[i] = s1[start + i];
		i++;
	}
	ptr[i] = '\0';
	return (ptr);
}

char	*ft_strtrim(char const *s1, char const *set)
{
	size_t	start;
	size_t	end;
	size_t	len;

	if (!s1 || !set)
		return (NULL);
	len = ft_strlen(s1);
	start = countstart(s1, set);
	end = countend(s1, set);
	return (trim_alloc(s1, start, end, len));
}
