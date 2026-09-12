/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstadd_front.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eabushak <eabushak@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/06 10:42:41 by eabushak          #+#    #+#             */
/*   Updated: 2025/12/06 12:47:56 by eabushak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstadd_front(t_list **lst, t_list	*new)
{
	if (new == NULL)
		return ;
	if (*lst == NULL)
		new -> next = NULL;
	else
		new -> next = *lst;
	*lst = new;
}
